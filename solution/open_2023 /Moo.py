
def solve(commas: int, periods:int, words_type_list: dict) -> None:
    # print(f'{commas=} {periods=}')
    # print(f'{words_type_list=}')
    nouns = len(words_type_list['noun'])
    transitives = len(words_type_list['transitive-verb'])
    intransitives = len(words_type_list['intransitive-verb'])
    conjunctions = len(words_type_list['conjunction'])
    # print(f'{nouns=} {transitives=} {intransitives=} {conjunctions=}')

    sentences_intransitives = list()
    sentences_transitives = list()
    sentences_compound = list()
    words_used = nouns + transitives + intransitives + conjunctions
    # Step 1: try to make more sentences: first type 1: noun+intransitives, then type 2 noun + transitive verb + noun(s)
    # the reason is type 1 sentences use more nouns. For example, 2 nouns can make A1, B2, but A1B.
    while len(words_type_list['noun']) > 0 and len(words_type_list['intransitive-verb']) > 0:
        sentences_intransitives.append(words_type_list['noun'][-1] + ' ' + words_type_list['intransitive-verb'][-1])
        words_type_list['noun'].pop()
        words_type_list['intransitive-verb'].pop()
    while len(words_type_list['noun']) > 1 and len(words_type_list['transitive-verb']) > 0:
        sentences_transitives.append(words_type_list['noun'][-1] + ' ' + words_type_list['transitive-verb'][-1] +
                                     ' ' + words_type_list['noun'][-2])
        words_type_list['noun'].pop()
        words_type_list['noun'].pop()
        words_type_list['transitive-verb'].pop()

    # The most possible sentences (sentences_possible) we can make is either (periods + conjunctions) if conjunctions <= periods;
    # or (periods + periods) if conjunctions > periods
    sentences_possible = periods
    if conjunctions >= periods: sentences_possible += periods
    else: sentences_possible += conjunctions
    
    # Step 2.A :so decompose type 1 [noun + intransitives] sentences if necessary to make more nouns available.
    # the order is important. We want to keep type 2 sentences because one sentence uses 3 words. type 1 sentence uses 2 words.
    sentences_decompose = len(sentences_intransitives) + len(sentences_transitives) - sentences_possible
    while len(sentences_intransitives) > 0 and sentences_decompose > 0:
        noun, v = sentences_intransitives[-1].split()
        words_type_list['noun'].append(noun)
        words_type_list['intransitive-verb'].append(v)
        sentences_intransitives.pop()
        sentences_decompose -= 1
    # Step 2.B: decompose type 2 [noun + transitive + noun] sentences if necessary to make more nouns available.
    while len(sentences_transitives) > 0 and sentences_decompose > 0:
        noun1, v, noun2 = sentences_transitives[-1].split()
        words_type_list['noun'].append(noun1)
        words_type_list['noun'].append(noun2)
        words_type_list['transitive-verb'].append(v)
        sentences_transitives.pop()
        sentences_decompose -= 1

    # Step 3.A replace type 1 sentences with type 2 sentences, if possible. so more nouns are used.
    # Step 3.A vs Step 3.B order does not matter.
    while len(words_type_list['noun']) > 0 and len(words_type_list['transitive-verb']) > 0 \
            and len(sentences_intransitives) > 0:
        noun, v = sentences_intransitives[-1].split()
        words_type_list['intransitive-verb'].append(v)
        sentences_intransitives.pop()
        sentences_transitives.append(noun + ' ' + words_type_list['transitive-verb'][-1] + ' ' +
                                     words_type_list['noun'][-1])
        words_type_list['noun'].pop()
        words_type_list['transitive-verb'].pop()

    # Step 3.B add ','+ noun to sentences
    while len(words_type_list['noun']) > 0 and commas > 0 and len(sentences_transitives) > 0:
        sentence_commas = sentences_transitives[-1]
        sentences_transitives.pop()
        sentence_commas = sentence_commas + ', '+words_type_list['noun'][-1]
        sentences_transitives.append(sentence_commas)
        words_type_list['noun'].pop()
        commas -= 1

    # Step 4 compose sentences
    sentences_to_join = sentences_intransitives + sentences_transitives
    while len(words_type_list['conjunction']) > 0 and len(sentences_to_join) > 1:
        sentences_compound.append(sentences_to_join[-1] + ' ' + words_type_list['conjunction'][-1]
                                  + ' ' + sentences_to_join[-2]+'.')
        words_type_list['conjunction'].pop()
        sentences_to_join.pop()
        sentences_to_join.pop()

    # Step 5 join sentences
    sentences_compound_str = ''
    if len(sentences_compound): sentences_compound_str = ' '.join(sentences_compound)
    
    sentences_to_join_str = ''
    sentences_to_join = [ x+'.' for x in sentences_to_join]
    if len(sentences_to_join): sentences_to_join_str = ' '.join(sentences_to_join) 

    words_left = len(words_type_list['noun']) + len(words_type_list['transitive-verb']) + \
                 len(words_type_list['intransitive-verb']) + len(words_type_list['conjunction'])
    words_used -= words_left

#    print(f'{sentences_intransitives=} {sentences_transitives=} {sentences_compound=} {words_used=}')
#    print(f"{words_type_list['noun']=} {words_type_list['intransitive-verb']=} "
#         f"{words_type_list['conjunction']=} {words_type_list['transitive-verb']=} \n\n")

    print(words_used)
        
    res=sentences_compound_str
    if sentences_to_join_str:
        if sentences_compound_str: res+= ' '+sentences_to_join_str
        else: res = sentences_to_join_str
    
    print(res)


T = int(input())
for i in range(T):
    N, commas, periods = [int(x) for x in input().split()]
    words_type_list = dict()
    words_type_list['noun'] = list()
    words_type_list['transitive-verb'] = list()
    words_type_list['intransitive-verb'] = list()
    words_type_list['conjunction'] = list()
    for j in range(N):
        word, word_type = input().rstrip().split()
        words_type_list[word_type].append(word)
    solve(commas, periods, words_type_list)
