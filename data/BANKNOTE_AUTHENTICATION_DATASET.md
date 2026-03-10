# Banknote Authentication Dataset

This file describes the **Banknote Authentication** dataset used in this project.

## Source

- **Dataset:** Banknote Authentication
- **UCI Machine Learning Repository:** https://archive.ics.uci.edu/dataset/267/banknote+authentication

## Description

The dataset contains features extracted from images of genuine and forged banknote-like specimens. Each banknote is represented by four features derived from wavelet transformed images.

## Data Format

The dataset is provided as a CSV file in `data/data_banknote_authentication.csv`.

Each row contains the following columns (in order):

1. **variance** of Wavelet Transformed image (continuous)
2. **skewness** of Wavelet Transformed image (continuous)
3. **curtosis** of Wavelet Transformed image (continuous)
4. **entropy** of image (continuous)
5. **class** (integer):
   - `0` = authentic
   - `1` = inauthentic

## Usage

This dataset is commonly used for binary classification experiments to distinguish between genuine and forged banknotes.

## Notes

- The dataset has no missing values.
- Each row is a distinct banknote observation.
- The data was originally collected from genuine and forged banknote images using wavelet transform feature extraction.
