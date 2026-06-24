"""
Natural examples demonstrating what TRIBE v2 and LLM-only models
activate in the brain for the same real-world stimuli.
"""
from benchmark_data import NATURAL_EXAMPLES


def print_natural_examples():
    print('\n' + '=' * 72)
    print(f'{"TRIBE v2 vs LLM — Natural Examples Brain Coverage":^72}')
    print('=' * 72)

    for i, ex in enumerate(NATURAL_EXAMPLES, 1):
        s  = ex['stimulus']
        dm = ex['dominant']
        tr = ex['tribe_r']
        lr = ex['llm_r']
        tc = ex['tribe_covers']
        lc = ex['llm_covers']
        print(f'\n[{i}] {s} (dominant modality: {dm})')
        print(f'    TRIBE v2 (r={tr:.2f}): {tc}')
        print(f'    LLM-only (r={lr:.2f}): {lc}')
        print(f'    Advantage: TRIBE v2 is {tr/max(lr, 0.01):.1f}x better at predicting brain responses')

    print('\n' + '=' * 72)
    print('Key takeaway: LLM-only models are essentially blind to visual and auditory cortex.')
    print('TRIBE v2 captures the full multimodal brain response.')


if __name__ == '__main__':
    print_natural_examples()
