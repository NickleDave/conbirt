<br>
<div align="center">
<img src="https://github.com/vocalpy/crowsetta/blob/main/doc/_static/crowsetta-primary-logo.png?raw=True" width="400">
</div>
<hr>

## A Python tool to work with any format for annotating animal vocalizations and bioacoustics data

[![Build Status](https://github.com/NickleDave/crowsetta/actions/workflows/ci.yml/badge.svg)](https://github.com/NickleDave/crowsetta/actions)
[![Documentation Status](https://readthedocs.org/projects/crowsetta/badge/?version=latest)](https://crowsetta.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/159904494.svg)](https://zenodo.org/badge/latestdoi/159904494)
[![PyPI version](https://badge.fury.io/py/crowsetta.svg)](https://badge.fury.io/py/crowsetta)
[![codecov](https://codecov.io/gh/NickleDave/crowsetta/branch/main/graph/badge.svg?token=TXtNTxXKmb)](https://codecov.io/gh/NickleDave/crowsetta)

crowsetta provides a Pythonic way to work with annotation formats 
for animal vocalizations and bioacoustics data. 
These formats are used, for example, by 
applications that enable users to annotate audio and/or spectrograms. 
Such annotations typically include the times when sound events start and stop, 
and labels that assign each sound to some set of classes 
chosen by the annotator.
crowsetta has built-in support for many widely used 
[formats](https://crowsetta.readthedocs.io/en/latest/formats/index.html),
such as 
[Audacity label tracks](https://crowsetta.readthedocs.io/en/latest/formats/seq/aud-txt.html#aud-txt), 
[Praat .TextGrid files](https://crowsetta.readthedocs.io/en/latest/formats/seq/textgrid.html#textgrid), 
and [Raven .txt files](https://crowsetta.readthedocs.io/en/latest/formats/bbox/raven.html#raven).

---

<img align="left"
width="600"
alt="example spectrogram showing Bengalese finch song with Praat TextGrid annotations indicated as segments underneath"
src="https://github.com/vocalpy/crowsetta/blob/main/doc/_static/example-textgrid-for-index.png?raw=True">

Spectrogram of the song of a Bengalese finch 
with syllables annotated as segments underneath. 
Annotations parsed by crowsetta 
from a file in the Praat .TextGrid  format.
Example song from 
[Bengalese finch song dataset](https://osf.io/r6paq/), 
Tachibana and Morita 2021, adapted under 
CC-By-4.0 License.

<br>

<br>

---

<img align="left"
width="600"
alt="example spectrogram from field recording with Raven annotations of birdsong indicated as rectangular bounding boxes"
src="https://github.com/vocalpy/crowsetta/blob/main/doc/_static/example-raven-for-index.png?raw=True">

Spectrogram of a field recording 
with annotations of songs of different bird species
indicated as bounding boxes.
Annotations parsed by crowsetta 
from a file in the 
[Raven Selection Table](https://crowsetta.readthedocs.io/en/latest/formats/bbox/raven.html#raven) 
format.
Example song from 
["An annotated set of audio recordings of Eastern North American birds containing frequency, time, and species information"](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecy.3329), 
Chronister et al., 2021, adapted under 
CC0 1.0 License.

---

Who would want to use crowsetta?
Anyone that works with animal vocalizations 
or other bioacoustics data that is annotated in some way.
Maybe you are a neuroscientist trying to figure out how songbirds learn their song,
or why mice emit ultrasonic calls. Or maybe you're an ecologist studying dialects of finches
distributed across Asia, or maybe you are a linguist studying accents in the
Caribbean, or a speech pathologist looking for phonetic changes that indicate early onset
Alzheimer's disease. crowsetta makes it easier for you to work with 
your annotations in Python, regardless of the format.

## Features

* take advantage of built-in support 
  for many widely used
  [formats](https://crowsetta.readthedocs.io/en/latest/formats/index.html),
  such as 
  [Audacity label tracks](https://crowsetta.readthedocs.io/en/latest/formats/seq/aud-txt.html#aud-txt), 
  [Praat .TextGrid files](https://crowsetta.readthedocs.io/en/latest/formats/seq/textgrid.html#textgrid), 
  and [Raven .txt files](https://crowsetta.readthedocs.io/en/latest/formats/bbox/raven.html#raven).
* work with any format by remembering just one class:  
  `annot = crowsetta.Transcriber(format='format').from_file('annotations.ext')`
  - no need to remember different functions for different formats 
* when needed, use classes that represent the formats 
  to write readable scripts and libraries 
* convert annotations to common file formats like `.csv`
  that anyone can work with
* work with custom formats that are not built in to `crowsetta` 
  by writing simple classes, leveraging abstractions 
  that can represent a wide array of annotation formats

For examples of these features, please see: https://crowsetta.readthedocs.io/en/latest/index.html#features

## Getting Started
### Installation
#### with `pip`

```console
$ pip install crowsetta
```

#### with `conda`

```console
$ conda install crowsetta -c conda-forge
```

### Usage

If you are new to crowsetta, start with 
[tutorial](https://crowsetta.readthedocs.io/en/latest/tutorial.html).

For vignettes showing how to use crowsetta for various tasks, 
such as working with your own annotation format, 
please see the [how-to](https://crowsetta.readthedocs.io/en/latest/howto.html)
section.

## Project Information

### Background

crowsetta was developed for two libraries:
- `hybrid-vocal-classifier` <https://github.com/vocalpy/hybrid-vocal-classifier>
- `vak` <https://github.com/vocalpy/vak>

### Support

To report a bug or request a feature (such as a new annotation format), 
please use the issue tracker on GitHub:  
<https://github.com/vocalpy/crowsetta/issues>

To ask a question about crowsetta, discuss its development, 
or share how you are using it, 
please start a new topic on the VocalPy forum 
with the crowsetta tag:  
<https://forum.vocalpy.org/>

### Contribute

- Issue Tracker: <https://github.com/vocalpy/crowsetta/issues>
- Source Code: <https://github.com/vocalpy/crowsetta>

### CHANGELOG
You can see project history and work in progress in the [CHANGELOG](./doc/CHANGELOG.md)

### License

The project is licensed under the [BSD license](./LICENSE).

### Citation
If you use crowsetta, please cite the DOI:
[![DOI](https://zenodo.org/badge/159904494.svg)](https://zenodo.org/badge/latestdoi/159904494)
