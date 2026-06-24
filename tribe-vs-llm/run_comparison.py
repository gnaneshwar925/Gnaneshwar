"""
CLI script: run the full TRIBE v2 vs LLM benchmark and generate all 6 visualizations.

Usage:
    python run_comparison.py
    python run_comparison.py --save-dir ./charts
"""
import argparse
import sys

import benchmark_data as data
from visualizations import run_all_visualizations


def print_summary(d):
    import numpy as np
    print('=' * 72)
    print(f'{"TRIBE v2 vs LLM vs Previous SOTA — BENCHMARK SUMMARY":^72}')
    print('=' * 72)
    print(f'{"Brain Region":<26} {"TRIBE v2":>10} {"Prev SOTA":>10} {"LLM-only":>10} {"TRIBE Gain":>12}')
    print('-' * 72)
    for region, t, s, l in zip(d.BRAIN_REGIONS_FLAT, d.TRIBE_R, d.SOTA_R, d.LLM_R):
        print(f'{region:<26} {t:>10.3f} {s:>10.3f} {l:>10.3f} {t - l:>+11.3f}')
    print('-' * 72)
    import numpy as np
    t_avg = np.mean(d.TRIBE_R)
    s_avg = np.mean(d.SOTA_R)
    l_avg = np.mean(d.LLM_R)
    print(f'{"AVERAGE":<26} {t_avg:>10.3f} {s_avg:>10.3f} {l_avg:>10.3f} {t_avg - l_avg:>+11.3f}')
    print('=' * 72)
    print(f'\nSpatial Resolution: TRIBE v2 predicts {d.TRIBE_VERTICES:,} vertices vs {d.SOTA_VERTICES} in previous SOTA')
    print(f'Resolution gain: {d.RESOLUTION_GAIN}x improvement')
    import numpy as np
    print(f'Zero-shot avg: TRIBE {np.mean(d.TRIBE_ZEROSHOT):.3f} | SOTA {np.mean(d.SOTA_ZEROSHOT):.3f} | LLM {np.mean(d.LLM_ZEROSHOT):.3f}')
    print()
    print('Natural Examples:')
    print(f'{"Stimulus":<28} {"Dominant":>10} {"TRIBE r":>8} {"LLM r":>7} {"Gain":>8}')
    print('-' * 68)
    for ex in d.NATURAL_EXAMPLES:
        s  = ex['stimulus']
        dm = ex['dominant']
        tr = ex['tribe_r']
        lr = ex['llm_r']
        print(f'{s:<28} {dm:>10} {tr:>8.2f} {lr:>7.2f} {tr - lr:>+8.2f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TRIBE v2 vs LLM Benchmark')
    parser.add_argument('--save-dir', default='.', help='Directory to save chart PNGs')
    args = parser.parse_args()

    print_summary(data)
    print('\nGenerating all 6 visualizations...')
    run_all_visualizations(data)
    print(f'Charts saved to {args.save_dir}/')
