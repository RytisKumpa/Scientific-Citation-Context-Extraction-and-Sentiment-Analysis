# Scientific-Citation-Context-Extraction-and-Sentiment-Analysis
This repository contains labeled data sets for Scientific Citation Context Extraction and Sentiment Analysis.

The text used for labeling has been tokenized and certain text has been replaced with the following tokens:
- `<MATH>`       - Mathematics.
- `<TABLE>`      - Table.
- `<REMARK>`     - Remark.
- `<THEOREM>`    - Theorem.
- `<TARGET_CIT>` - Target citation.

The samples in the Citation Context data set have been formatted as follows:

*This###CONT is###CONT a###CONT sample###CONT citation###CIT .###OTHER This###NCONT is###NCONT a###NCONT sentence###NCONT outside###NCONT of###NCONT the###NCONT citation###NCONT context###NCONT .###OTHER*

where the token is sperated from the label using ###. The labels are:
- CONT  - Citation context.
- CIT   - Target citation.
- NCONT - Text outside of the citation context.
- OTHER - Other characters.

ContextVizualizer.py can be used to display the tagged citation context in an easy-to-read format. Citation context is displayed in greem, non-context in red, and the target citation in blue.

The samples in the Citation Sentiment data set have been formatted as follows:

*p  This is a citation carrying positive sentiment .*

The citation sentiment is classified into:
- o - Neutral
- p - Positive
- n - Negative
