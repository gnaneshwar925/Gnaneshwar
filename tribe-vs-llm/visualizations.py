"""
Visualization functions for TRIBE v2 vs LLM benchmark comparison.
All charts use pre-computed benchmark data from benchmark_data.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import seaborn as sns
from math import pi

plt.rcParams['figure.dpi'] = 130
plt.rcParams['font.size'] = 11
sns.set_theme(style='whitegrid')

TRIBE_COLOR = '#1565C0'
LLM_COLOR   = '#B71C1C'
SOTA_COLOR  = '#558B2F'


def viz1_brain_encoding_accuracy(brain_regions, tribe_r, llm_r, sota_r, save=True):
    """Grouped bar chart: brain encoding accuracy across 5 regions."""
    fig, ax = plt.subplots(figsize=(13, 6))
    x, w = np.arange(len(brain_regions)), 0.26

    b1 = ax.bar(x - w,   tribe_r, w, label='TRIBE v2 (Trimodal)', color=TRIBE_COLOR, alpha=0.9)
    b2 = ax.bar(x,       sota_r,  w, label='Previous SOTA',        color=SOTA_COLOR,  alpha=0.9)
    b3 = ax.bar(x + w,   llm_r,   w, label='LLM-only (Text)',      color=LLM_COLOR,   alpha=0.9)

    for bars, col in [(b1, TRIBE_COLOR), (b2, SOTA_COLOR), (b3, LLM_COLOR)]:
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.004,
                    f'{b.get_height():.2f}', ha='center', va='bottom',
                    fontsize=8.5, color=col, fontweight='bold')

    ax.set_xlabel('Brain Region', fontsize=12)
    ax.set_ylabel('Encoding Score (Pearson r)', fontsize=12)
    ax.set_title('Visualization 1 — Brain Encoding Accuracy by Region:\nTRIBE v2 vs LLM-only vs Previous SOTA',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(brain_regions, fontsize=11)
    ax.set_ylim(0, 0.78)
    ax.legend(fontsize=11)
    ax.axhline(0, color='black', linewidth=0.4)
    plt.tight_layout()
    if save:
        plt.savefig('viz1_brain_encoding_accuracy.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f'TRIBE avg: {np.mean(tribe_r):.3f}  |  LLM avg: {np.mean(llm_r):.3f}  |  SOTA avg: {np.mean(sota_r):.3f}')


def viz2_spatial_resolution(tribe_verts, sota_verts, save=True):
    """Bar chart + cortical coverage scatter: 70x spatial resolution improvement."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    bars = ax.bar(['Previous SOTA', 'TRIBE v2'], [sota_verts, tribe_verts],
                  color=[SOTA_COLOR, TRIBE_COLOR], alpha=0.9, width=0.5)
    ax.set_ylabel('Cortical Vertices Predicted', fontsize=11)
    ax.set_title('Spatial Resolution Comparison', fontsize=12, fontweight='bold')
    ax.set_ylim(0, tribe_verts * 1.25)
    for bar, val, col in zip(bars, [sota_verts, tribe_verts], [SOTA_COLOR, TRIBE_COLOR]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 200,
                f'{val:,}', ha='center', fontsize=12, fontweight='bold', color=col)
    gain = tribe_verts // sota_verts
    ax.annotate(f'{gain}x improvement', xy=(1, tribe_verts * 0.5),
                ha='center', fontsize=14, fontweight='bold', color=TRIBE_COLOR)

    ax2 = axes[1]
    theta = np.linspace(0, 2 * np.pi, 200)
    ax2.fill(np.cos(theta), np.sin(theta), alpha=0.10, color='gray')
    ax2.plot(np.cos(theta), np.sin(theta), color='gray', linewidth=1)
    rng = np.random.default_rng(42)
    pts = rng.uniform(-0.95, 0.95, (600, 2))
    mask = pts[:, 0] ** 2 + pts[:, 1] ** 2 < 0.90
    ax2.scatter(pts[mask, 0], pts[mask, 1], s=3, c=TRIBE_COLOR, alpha=0.55,
                label=f'TRIBE v2 (~{tribe_verts:,} vertices)')
    pts2 = rng.uniform(-0.95, 0.95, (20, 2))
    mask2 = pts2[:, 0] ** 2 + pts2[:, 1] ** 2 < 0.90
    ax2.scatter(pts2[mask2, 0], pts2[mask2, 1], s=90, c=SOTA_COLOR, marker='X',
                alpha=0.95, label=f'Previous SOTA (~{sota_verts} voxels)')
    ax2.set_xlim(-1.3, 1.3)
    ax2.set_ylim(-1.3, 1.3)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Cortical Coverage Illustration', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10, loc='lower center')

    fig.suptitle('Visualization 2 — Spatial Resolution: 70x Improvement in Cortical Coverage',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    if save:
        plt.savefig('viz2_spatial_resolution.png', dpi=150, bbox_inches='tight')
    plt.show()


def viz3_radar_chart(radar_cats, tribe_radar, llm_radar, sota_radar, save=True):
    """Radar / spider chart across 6 capability dimensions."""
    N = len(radar_cats)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

    for vals, col, lbl, ls in [
        (tribe_radar, TRIBE_COLOR, 'TRIBE v2',        '-'),
        (sota_radar,  SOTA_COLOR,  'Previous SOTA',   '--'),
        (llm_radar,   LLM_COLOR,   'LLM-only',        ':'),
    ]:
        v = vals + vals[:1]
        ax.plot(angles, v, ls, linewidth=2.5, color=col, label=lbl)
        ax.fill(angles, v, alpha=0.10, color=col)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(radar_cats, fontsize=11)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=8, color='gray')
    ax.set_title('Visualization 3 — Multi-Metric Radar Chart',
                 fontsize=13, fontweight='bold', pad=30)
    ax.legend(loc='upper right', bbox_to_anchor=(1.38, 1.15), fontsize=12)
    plt.tight_layout()
    if save:
        plt.savefig('viz3_radar_chart.png', dpi=150, bbox_inches='tight')
    plt.show()


def viz4_brain_region_heatmap(heatmap_data, heatmap_models, heatmap_regions, save=True):
    """Heatmap: brain encoding score per model per brain region."""
    fig, ax = plt.subplots(figsize=(11, 5))
    df = pd.DataFrame(heatmap_data, index=heatmap_models, columns=heatmap_regions)
    sns.heatmap(df, ax=ax, annot=True, fmt='.2f', cmap='YlOrRd',
                linewidths=0.5, linecolor='white',
                cbar_kws={'label': 'Brain Encoding Score (Pearson r)', 'shrink': 0.8},
                vmin=0.1, vmax=0.7)
    ax.set_title('Visualization 4 — Brain Region Encoding Heatmap\n'
                 '(Pearson r: LLM-only is blind to visual and auditory cortex)',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel('Model', fontsize=11)
    ax.set_xlabel('Brain Region', fontsize=11)
    plt.tight_layout()
    if save:
        plt.savefig('viz4_brain_region_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()


def viz5_modality_ablation(ablation_labels, ablation_scores, save=True):
    """Bar chart: modality ablation — contribution of each encoder."""
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = [TRIBE_COLOR, '#5C6BC0', '#42A5F5', '#80DEEA', LLM_COLOR]
    bars = ax.bar(ablation_labels, ablation_scores, color=colors, alpha=0.90,
                  edgecolor='white', linewidth=0.8)
    for bar, val in zip(bars, ablation_scores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                f'r={val:.3f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel('Avg Brain Encoding Score (Pearson r)', fontsize=12)
    ax.set_title('Visualization 5 — Modality Ablation: Contribution of Each Encoder',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_ylim(0, 0.72)
    ax.axhline(ablation_scores[0], color=TRIBE_COLOR, linestyle='--', alpha=0.45, linewidth=1.5)
    ax.annotate('Full TRIBE v2 baseline', xy=(0, ablation_scores[0]),
                xytext=(2.5, 0.60), fontsize=10, color=TRIBE_COLOR,
                arrowprops=dict(arrowstyle='->', color=TRIBE_COLOR, lw=1.5))
    plt.tight_layout()
    if save:
        plt.savefig('viz5_modality_ablation.png', dpi=150, bbox_inches='tight')
    plt.show()
    drop_video = ablation_scores[0] - ablation_scores[1]
    drop_audio = ablation_scores[0] - ablation_scores[2]
    drop_text  = ablation_scores[0] - ablation_scores[3]
    print(f'Removing video drops score by {drop_video:.3f}')
    print(f'Removing audio drops score by {drop_audio:.3f}')
    print(f'Removing text  drops score by {drop_text:.3f}')


def viz6_zeroshot_generalization(subjects, tribe_z, llm_z, sota_z, save=True):
    """Grouped bar chart: zero-shot generalization across 8 held-out subjects."""
    fig, ax = plt.subplots(figsize=(13, 6))
    x, w = np.arange(len(subjects)), 0.26
    b1 = ax.bar(x - w, tribe_z, w, label='TRIBE v2',      color=TRIBE_COLOR, alpha=0.9)
    b2 = ax.bar(x,     sota_z,  w, label='Previous SOTA', color=SOTA_COLOR,  alpha=0.9)
    b3 = ax.bar(x + w, llm_z,   w, label='LLM-only',      color=LLM_COLOR,   alpha=0.9)
    ax.set_xlabel('Held-Out Test Subject', fontsize=12)
    ax.set_ylabel('Zero-Shot Encoding Score (Pearson r)', fontsize=12)
    ax.set_title('Visualization 6 — Zero-Shot Generalization Across Unseen Subjects\n'
                 '(trained on other subjects, no fine-tuning on test subjects)',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(subjects, fontsize=11)
    ax.set_ylim(0, 0.58)
    ax.legend(fontsize=11)
    ax.axhline(np.mean(tribe_z), color=TRIBE_COLOR, linestyle='--', alpha=0.4, linewidth=1.3)
    ax.axhline(np.mean(llm_z),   color=LLM_COLOR,   linestyle='--', alpha=0.4, linewidth=1.3)
    plt.tight_layout()
    if save:
        plt.savefig('viz6_zeroshot_generalization.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f'TRIBE avg: {np.mean(tribe_z):.3f} | SOTA avg: {np.mean(sota_z):.3f} | LLM avg: {np.mean(llm_z):.3f}')


def run_all_visualizations(data):
    """Run all 6 visualizations from a benchmark data module."""
    viz1_brain_encoding_accuracy(data.BRAIN_REGIONS, data.TRIBE_R, data.LLM_R, data.SOTA_R)
    viz2_spatial_resolution(data.TRIBE_VERTICES, data.SOTA_VERTICES)
    viz3_radar_chart(data.RADAR_CATS, data.TRIBE_RADAR, data.LLM_RADAR, data.SOTA_RADAR)
    viz4_brain_region_heatmap(data.HEATMAP_DATA, data.HEATMAP_MODELS, data.HEATMAP_REGIONS)
    viz5_modality_ablation(data.ABLATION_LABELS, data.ABLATION_SCORES)
    viz6_zeroshot_generalization(data.SUBJECTS, data.TRIBE_ZEROSHOT, data.LLM_ZEROSHOT, data.SOTA_ZEROSHOT)
