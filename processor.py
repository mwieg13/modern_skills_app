from data import UrlData



def find_index_of_section_test(tokens: list, section_name: str, index_from_before_section_name=False):
    foundIt = False
    index = -1
    section_name_tokens = section_name.split(' ')
    numSectionTokens = len(section_name_tokens)
    sectionTokensIndex = 0

    for token in tokens:
        index += 1

        if token == section_name_tokens[sectionTokensIndex]:
            sectionTokensIndex += 1

            # check if we've matched against all the tokens in section_name
            if sectionTokensIndex == numSectionTokens:
                index += 1
                foundIt = True
                break

        else:
            sectionTokensIndex = 0

    if foundIt:
        if index_from_before_section_name:
            index -= numSectionTokens
    else:
        index = -1
    
    return index


