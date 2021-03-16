bio_award(A) :-
        science_award(A),
        exists((award_received(P,A),
                occupation(P,wd:'Q864503'))).

bio_award_recipient(AN,PN,T,GN,AD) :-
        science_award(A),enlabel(A,AN),optional(en_description(A,AD)),
        award_received_at(P,A,T),enlabel(P,PN),
        sex_or_gender(P,G),enlabel(G,GN).

