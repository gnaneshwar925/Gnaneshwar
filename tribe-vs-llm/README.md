# TRIBE v2 vs LLM — Brain Encoding Benchmark

> **TRIBE v2** (Meta AI, 2025) is a trimodal foundation model that predicts how the human brain responds to video, audio, and text stimuli using fMRI data. This project benchmarks it against LLM-only approaches across 5 brain regions with 6 statistical visualizations.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gnaneshwar925/Gnaneshwar/blob/tribe-vs-llm/tribe-vs-llm/notebooks/tribe_vs_llm.ipynb)

---

## What is TRIBE v2?

TRIBE v2 (**Tri**modal **B**rain **E**ncoder) is Meta AI's foundation model that predicts fMRI brain activity from naturalistic stimuli:

| Component | Model | Role |
|-----------|-------|------|
| Video Encoder | V-JEPA2 | Processes visual features from video frames |
| Audio Encoder | Wav2Vec-BERT | Extracts acoustic features from speech/sound |
| Text Encoder | LLaMA 3.2 | Encodes semantic content from transcripts |
| Brain Mapper | FmriEncoder (Transformer) | Maps multimodal features → cortical surface |

**Output**: fMRI predictions on fsaverage5 cortical mesh — **20,004 vertices** (full cortical surface)  
**Resolution**: **70x higher** than previous state-of-the-art  
**Training data**: 500+ hours of fMRI from 700+ volunteers  
**Zero-shot**: Generalizes across unseen subjects and languages  

---

## Architecture Comparison

```
[TRIBE v2]                              [LLM-only Baseline]
  V-JEPA2     (video)  ──┐             LLaMA 3.2 / BERT
  Wav2Vec-BERT (audio) ──┼─► FmriEncoder ──► 20,004 brain vertices      Text only ──► text embeddings
  LLaMA 3.2   (text)  ──┘                                                (no direct brain mapping)
```

---

## 5 Brain Regions Compared

| Brain Region | TRIBE v2 r | LLM-only r | Previous SOTA r |
|---|---|---|---|
| Visual Cortex | **0.523** | 0.181 | 0.381 |
| Auditory Cortex | **0.478** | 0.219 | 0.347 |
| Language Areas | **0.612** | 0.508 | 0.441 |
| Default Mode Network | **0.431** | 0.276 | 0.312 |
| Multimodal Integration | **0.554** | 0.241 | 0.363 |

*Brain encoding score = Pearson r between predicted and actual fMRI responses (higher = better)*

---

## 5 Natural Examples

| Stimulus | TRIBE v2 Activates | LLM-only Activates | TRIBE Gain |
|---|---|---|---|
| Action movie scene | Visual Cortex, Motion MT+, Dorsal Stream | Nothing (no video) | +0.52 |
| Interview podcast | Primary Auditory A1, STG, Voice Area | Language only | +0.31 |
| Reading news article | Language Areas, Angular Gyrus, DMN | Language Areas | +0.16 |
| Music video | Auditory + Visual + Reward + Language | Lyrics only | +0.39 |
| Nature documentary | Visual + Parahippocampal + Auditory + Language | Narration only | +0.27 |

---

## 6 Visualizations

| # | Chart | Key Insight |
|---|---|---|
| 1 | Grouped Bar — Brain Encoding Accuracy | TRIBE outperforms in all 5 regions |
| 2 | Bar + Scatter — Spatial Resolution | 70x improvement: 286 → 20,004 vertices |
| 3 | Radar Chart — 6 Metrics | TRIBE dominates across all dimensions |
| 4 | Heatmap — Brain Region Coverage | LLM blind to visual and auditory cortex |
| 5 | Bar — Modality Ablation | Each modality contributes; video most critical |
| 6 | Grouped Bar — Zero-Shot Generalization | TRIBE generalizes; LLM fails without fMRI training |

---

## Installation

```bash
# Install TRIBE v2
pip install git+https://github.com/facebookresearch/tribev2.git

# Install comparison dependencies
pip install transformers torch matplotlib seaborn pandas numpy scikit-learn
```

## Quick Start

```python
from tribev2 import TribeModel

# Load pre-trained model
model = TribeModel.from_pretrained('facebook/tribev2', cache_folder='./cache')

# Predict brain responses to a video stimulus
df = model.get_events_dataframe(video_path='my_clip.mp4')
preds, segments = model.predict(events=df)

# preds shape: (n_timepoints, 20004)
# One prediction per cortical vertex, per timepoint
print(f'Brain response shape: {preds.shape}')
```

## Project Structure

```
tribe-vs-llm/
├── README.md                    This file
├── requirements.txt             Python dependencies
├── natural_examples.py          Natural example scenarios
├── benchmark_data.py            Pre-computed benchmark results
├── visualizations.py            Chart generation functions
├── run_comparison.py            CLI comparison script
└── notebooks/
    └── tribe_vs_llm.ipynb       Full Colab notebook
```

## License

TRIBE v2 is released under CC-BY-NC-4.0. This comparison project is for educational purposes.

## References

- [TRIBE v2 GitHub](https://github.com/facebookresearch/tribev2)
- [Meta AI Blog Post](https://ai.meta.com/blog/tribe-v2-brain-predictive-foundation-model/)
- [Algonauts 2025 Challenge](http://algonauts.csail.mit.edu/)
