
# PatStat Fuzzy Matching

## Introduction

This repository contains the code and documentation for the creation of a dataset that connects firms and their intellectual properties. This work is part of a broader research project investigating the correlation between patent ownership and company performance.

## Datasets

Two datasets were merged to generate the research database:
- **CrunchBase Extraction:** Contains 1,476 firms with details such as brand name, description, geographical location, website URL, and founding year.
- **PatStat 2021 Database:** A European Union-generated database tracking intellectual property applicants. It contains 9,981,853 applicants as of Autumn 2021.

## Fuzzy Merging Procedure

The company names recorded in PatStat often differ from their commercially registered names due to misspellings, omitted corporate forms, or unnecessary capitalization. Therefore, a fuzzy matching approach was implemented. The process consists of:
1. **Pre-processing** of the datasets.
2. **Fuzzy matching** of firm names with applicant names.
3. **Disambiguation** of the matched data.

## Pre-Processing

### CrunchBase Extraction Pre-Processing
- Missing country data was manually resolved using firm headquarters' locations.
- Country names were standardized into country codes using `pycountry`.

### PatStat Database Pre-Processing
- The relevant tables (`tls206 part 1 & 2`) were imported and concatenated.
- Data was filtered to retain only companies (excluding individuals).
- Missing country codes were replaced with "XX".

### Company Name Standardization
- Names were capitalized and stripped of non-alphanumeric characters.
- Legal designations were standardized (e.g., "Laboratories" → "Lab").

## Fuzzy Matching

### Approaches Used
1. **Exact Matching**
   - Firms and applicants were linked if their names were identical.
   - Match Type: `Alphanumeric`
   
2. **Jaro-Winkler Similarity Matching**
   - Measures similarity between two strings (score range: 0–1).
   - Matches with a score above 0.9 were retained.
   - Match Type: `Jaro-Winkler`

3. **Levenshtein Distance Matching**
   - Calculates the minimum number of edits needed to change one string into another.
   - Matches with an edit distance ≤ 3 were retained.
   - Match Type: `Levenshtein`

## Disambiguation Process

To ensure each firm maps to exactly one applicant, a scoring system was applied:

### Quality of Match Score
1. **Location Score**
   - 1: Same country
   - 2: Missing location
   - 3: Different country
   
2. **Match Type Score**
   - 1: Exact Matching
   - 2: Jaro-Winkler
   - 3: Levenshtein

### Optimality Score Calculation
The optimality score was computed as:
```
Optimality Score = sqrt(Location Score² + Match Type Score²)
```
A lower score indicates a higher likelihood of a correct match.

### Two-Side Selection Process
Matches were selected iteratively, ensuring each firm is linked to only one applicant, prioritizing the most reliable matches.

## Final Output

The final dataset includes:
- CrunchBase company ID, name, country, founding year
- PatStat applicant ID, name, address, country
- Match type and filtering criteria

## Opportunities for Further Improvement

- Implement industry-based filtering criteria.
- Utilize IPC class data to refine patent-industry relationships.

## References

1. Tarasconi, G., & Menon, C. (2017). *Matching Crunchbase with patent data.*
2. Arora, A., Belenzon, S., & Sheer, L. (2021). *Matching patents to compustat firms, 1980–2015: Dynamic reassignment, name changes, and ownership structures.* Research Policy, 50(5), 104217.
