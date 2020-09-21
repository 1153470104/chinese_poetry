from jiayan import PMIEntropyLexiconConstructor

constructor = PMIEntropyLexiconConstructor()
lexicon = constructor.construct_lexicon('raw_multi_line.txt')
constructor.save(lexicon, 'model.csv')
