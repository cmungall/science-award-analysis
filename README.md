# Science awards analysis

See results:

 * [results/science-awards-summary.tsv](results/science-awards-summary.tsv)

There should be one row for every award in Wikidata

For each award, we breakdown the number of awardees by gender. We also
do a binomial test for bias. This is not yet broken down by dates of
award. As expected awards that started earlier display worse bias.

## How this works

See [Makefile](Makefile}

We use sparqlprog to query a list of all award-awardee pairs from Wikidata, along with date of award

The python script in [src](src) uses pandas to summarize this
