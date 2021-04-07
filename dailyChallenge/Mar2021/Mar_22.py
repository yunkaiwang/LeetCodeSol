"""
Vowel spellchecker

O(m+n) time with O(m+n) space where
m is the number of words and n is
the number of queries. Nothing much
to say about the question, simply
put the word and the word after
removing vowels in the map and
check if match exists for each
query item.
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_map = {}
        approx_map = {}

        def replaceVowelWithStar(word):
            newWord = ""
            for c in word:
                if c not in "aeiou":
                    newWord += c
                else:
                    newWord += "*"

            return newWord

        for word in wordlist:
            exact_map[word] = word
            lower_word = word.lower()
            if lower_word not in approx_map:
                approx_map[lower_word] = word

            newWord = replaceVowelWithStar(lower_word)
            if newWord not in approx_map:
                approx_map[newWord] = word

        sol = []
        for query in queries:
            if query in exact_map:
                sol.append(query)
            elif query.lower() in approx_map:
                sol.append(approx_map[query.lower()])
            else:
                newWord = replaceVowelWithStar(query.lower())
                if newWord in approx_map:
                    sol.append(approx_map[newWord])
                else:
                    sol.append("")
        return sol