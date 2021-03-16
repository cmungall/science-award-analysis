# todo: header
results/science-awardees.tsv:
	pq-wikidata --consult src/awards.pro -f tsv  "bio_award_recipient(AN,PN,T,GN,AD)" > $@.tmp && sort -u -k1,3 $@.tmp > $@
.PRECIOUS: results/science-awardees.tsv
results/science-awards-summary.tsv: results/science-awardees.tsv
	python src/gender_analysis.py
