# Morphological complexity

The Heap's curve shows the dependence of the number of token types and the total number of tokens in a corpus. To draw the Heap's curve, we "read" the corpus from the beginning to the end and place new dots to the graph depending on whether each new token has already occured or not.


Figure 0. Heap's curves for corpora of different size.
![Figure 0](Figure_0.png)


We use the following formula to simulate the Heap's curve: <img src="https://render.githubusercontent.com/render/math?math=f(n) = f(n-1)%2B\sum_{i}p_i*(1-p_i)^{n-1}">. The main idea is that we first compile a frequency list and after that add tokens from this list to the graph according to their frequency.


Figure 1. Simulated Heap's curves for corpora of different size.
![Figure 1](Figure_1.png)

As can be seen from Figure 1, the Tokita curve started to coincide with the horisontal asymptote when it achieves 40,000 tokens (or even ealier). This is explained by the very small size of the Tokita corpus.

I manually cutted all the corpora (except Tokita), so that their size would be about 26,000 tokens.

Figure 2. Simulated Heap's curves for corpora of similar size.
![Figure 2](Figure_2.png)


Figures 3-4 show Zipf's curves (dependence of frequency of tokens from their rank) for corpora of different size and for corpora of similar size respectively.

Figure 3. Zipf's curves for corpora of different size.
![Figure 3](Figure_3.png)

Figure 3 (zoomed). Zipf's curves for corpora of different size.
![Figure 3 (zoomed](Figure_3_zoomed.png)

Figure 4. Zipf's curves for corpora of similar size.
![Figure 4](Figure_4.png)

Figure 4 (zoomed). Zipf's curves for corpora of similar size.
![Figure 4 (zoomed](Figure_4_zoomed.png)
