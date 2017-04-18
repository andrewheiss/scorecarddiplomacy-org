Title: Data, code, and analysis
Date: 2017-04-08
Modified: 2017-04-08 23:42:58
Excerpt: Something
Template: page
Slug: data


## Statistical analysis

The code for creating all the project's figures, tables, and analysis is available in a [version-controlled repository at GitHub](https://github.com/andrewheiss/scorecard-diplomacy). Everything in the book can be recreated using [R](https://www.r-project.org/), preferably within [RStudio](https://www.rstudio.com/), since the code is structured as an RStudio project.

This project uses data from dozens of different datasets and sources. All data can be accessed in the [project's GitHub repository](https://github.com/andrewheiss/scorecard-diplomacy/tree/master/data). The [most recent release of the project's source code](https://github.com/andrewheiss/scorecard-diplomacy/releases) also contains this data.


## NGO survey

The code to clean and process the survey data is available in the [GitHub repository](https://github.com/andrewheiss/From-the-Trenches-Anti-TIP-NGOs-and-US) for Andrew Heiss and Judith G. Kelley. 2016. "From the Trenches: A Global Survey of Anti-TIP NGOs and their Views of US Efforts." *Journal of Human Trafficking*. [doi:10.1080/23322705.2016.1199241](https://dx.doi.org/10.1080/23322705.2016.1199241)

The free response answers for respondents who requested anonymity have been
redacted. 

- CSV file: [`responses_full_anonymized.csv`](/files/data/responses_full_anonymized.csv)
- R file: [`responses_full_anonymized.rds`](/files/data/responses_full_anonymized.rds)


## Additional analysis and methods appendix

The book's [Methods Appendix](/files/pdfs/Judith%20Kelley%2C%20Scorecard%20Diplomacy%2C%20Methods%20Appendix.pdf) provides detailed information about the methods and data used, and it is available for free.

Much of the analysis and statistical modeling run for the project did not end up in the final book. Results from this additional analysis is available in two different notebooks:

- [`Replication and extension.pdf`](/files/pdfs/Replication%20and%20extension.pdf): Much of the statistical work in *Scorecard Diplomacy* is based on the models in Judith G. Kelley and Beth A. Simmons. 2015. "Politics by Number: Indicators as Social Pressure in International Relations." *American Journal of Political Science* 59, no. 1 (January): 55–70. [doi:10.1111/ajps.12119](http://dx.doi.org/10.1111/ajps.12119). The models in the article were created using Stata, and to ensure that the R-based results for the book were comparable, we first replicated the results from the article before expanding the models for the book's larger scope. This file shows the replicated results as well as the various iterations of expanded models that preceded the models that ultimately made it into the book.
- [`Interactions.pdf`](/files/pdfs/Interactions%20by%20treatment.pdf): Tables A7.1–5 and Figures A7.1–2 in the book's Results Appendix include the results from several statistical models that test the interaction of being present or downgraded in the annual TIP Report with the country's level of democracy. This file shows the results of dozens of other models testing for the interactive effects of 12 individual factors by presence in the TIP Report, receiving a lower rating, and being downgraded from the previous year.

---

## Content analysis

Many different sources were used for content analysis, including the annual [Trafficking in Persons (TIP) Report from the US State Department](https://www.state.gov/j/tip/rls/tiprpt/), US State Department diplomatic cables, and as documents from various intergovernmental and non-governmental organizations that deal with trafficking in persons. 

Media stories and State Department cables were loaded into qualitative data analysis software. QDA Miner is required to view this analysis, and is accessible either for free with [QDA Miner Lite](https://provalisresearch.com/products/qualitative-data-analysis-software/freeware/) (free) or with the [full version](https://provalisresearch.com/products/qualitative-data-analysis-software/).

Both cables and media stories were coded for reactions of officials to the annual TIP Report. The codes are explained in Chapter 4 in the book and can also be found in the [Methods Appendix](/files/pdfs/Judith%20Kelley%2C%20Scorecard%20Diplomacy%2C%20Methods%20Appendix.pdf).

### Cables

1. [`Scorecard Diplomacy.ppj`](/files/other/Public%20file%20of%20cables%20for%20Scorecard%20Diplomacy.ppj): This QDA Miner data file contains the qualitative codes and their descriptions for all official reactions to mentions of trafficking
2. [`Chapter 4 reactions.pdf`](/files/pdfs/Chapter%204%20reactions.pdf): contains the raw output of the reactions from Chapter 4

### Media stories

Four files are included with additional information:

1. [`Search details.txt`](/files/other/Search%20details.txt): contains the Lexis Nexis search queries used to identify media stories containing reactions to the TIP report
2. [`All stories.pdf`](/files/pdfs/All%20stories.pdf) contains 492 stories referencing the TIP report
3. [`Additional Watch List stories.pdf`](/files/pdfs/Additional%20Watch%20list%20stories.pdf): contains 98 stories referencing the Watch List
4. [`Media coverage.xlsx`](/files/other/Media%20coverage.xlsx): contains the raw data containing classification of media stories covering the TIP report
