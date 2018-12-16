import os
from glob import glob
import tempfile
import shutil
import csv
import unittest
from pathlib import Path, PureWindowsPath

import numpy as np
import evfuncs

import crowsetta

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))

ANNOT_DICT_FIELDNAMES = {'file': str,
                         'onsets_Hz': np.ndarray,
                         'offsets_Hz': np.ndarray,
                         'onsets_s': np.ndarray,
                         'offsets_s': np.ndarray,
                         'labels': np.ndarray}

SYL_DICT_FIELDNAMES = ['filename',
                       'onset_Hz',
                       'offset_Hz',
                       'onset_s',
                       'offset_s',
                       'label']


class TestNotmat(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = os.path.join(TESTS_DIR, 'test_data')
        self.tmp_output_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_output_dir)

    def test_notmat2seq(self):
        notmat = os.path.join(self.test_data_dir,
                              os.path.normpath(
                                  'cbins/gy6or6/032312/'
                                  'gy6or6_baseline_230312_0808.138.cbin.not.mat'))
        seq = crowsetta.notmat.notmat2seq(notmat)
        for fieldname, fieldtype in ANNOT_DICT_FIELDNAMES.items():
            self.assertTrue(hasattr(seq, fieldname))
            self.assertTrue(type(getattr(seq, fieldname)) == fieldtype)

    def test_notmat_list_to_csv(self):
        # since notmat_list_to_csv is basically a wrapper around
        # notmat2seq and seq2csv,
        # and those are tested above and in other test modules,
        # here just need to make sure this function doesn't fail
        cbin_dir = os.path.join(self.test_data_dir,
                                os.path.normpath('cbins/gy6or6/032312/'))
        notmat_list = glob(os.path.join(cbin_dir, '*.not.mat'))
        # below, sorted() so it's the same order on different platforms
        notmat_list = sorted(notmat_list)
        csv_filename = os.path.join(str(self.tmp_output_dir),
                                    'test.csv')
        crowsetta.notmat.notmat_list_to_csv(notmat_list, csv_filename)
        # make sure file was created
        assert os.path.isfile(csv_filename)

        # to be extra sure, make sure all filenames from
        # .not.mat list are in csv
        filenames_from_csv = []
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=SYL_DICT_FIELDNAMES)
            header = next(reader)
            for row in reader:
                filenames_from_csv.append(row['filename'])
        for notmat_name in notmat_list:
            cbin_name = notmat_name.replace('.not.mat', '')
            assert(cbin_name in filenames_from_csv)

    def test_make_notmat(self):
        cbin_dir = os.path.join(self.test_data_dir,
                                os.path.normpath('cbins/gy6or6/032312/'))
        notmat_list = glob(os.path.join(cbin_dir, '*.not.mat'))
        for notmat in notmat_list:
            seq = crowsetta.notmat.notmat2seq(notmat)
            notmat_dict = evfuncs.load_notmat(notmat)
            crowsetta.notmat.make_notmat(filename=seq.file,
                                         onsets_Hz=seq.onsets_Hz,
                                         offsets_Hz=seq.offsets_Hz,
                                         labels=np.asarray(list(notmat_dict['labels'])),
                                         samp_freq=notmat_dict['Fs'],
                                         threshold=notmat_dict['threshold'],
                                         min_syl_dur=notmat_dict['min_dur']/1000,
                                         min_silent_dur=notmat_dict['min_int']/1000,
                                         alternate_path=self.tmp_output_dir,
                                         other_vars=None
                                         )
            notmat_made = evfuncs.load_notmat(os.path.join(self.tmp_output_dir,
                                                           os.path.basename(notmat)))
            # can't do assert(new_dict == old_dict)
            # because headers will be different (and we want them to be different)
            for key in ['Fs', 'fname', 'labels', 'onsets', 'offsets',
                        'min_int', 'min_dur', 'threshold', 'sm_win']:
                if key == 'fname':
                    # have to deal with Windows path saved in .not.mat files
                    # and then compare file names without path to them
                    notmat_dict_path = PureWindowsPath(notmat_dict[key])
                    notmat_made_path = Path(notmat_made[key])
                    self.assertTrue(notmat_dict_path.name == notmat_made_path.name)
                elif type(notmat_dict[key]) == np.ndarray:
                    self.assertTrue(np.allclose(notmat_dict[key],
                                                notmat_made[key],
                                                atol=1e-3, rtol=1e-3))
                else:
                    self.assertTrue(notmat_dict[key] == notmat_made[key])


if __name__ == '__main__':
    unittest.main()
