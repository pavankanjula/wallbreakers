class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}  # Stores all the possible domain names with their number of occurances counts.
        for dom in cpdomains:
            domsplit = dom.replace(' ', '.').split('.')  # Splits each domain name
            for i in range(1, len(domsplit)):
                domname = ""
                for j in range(i, len(domsplit) - 1):  # makes all possible domain names
                    domname = domname + domsplit[j] + '.'
                domname += domsplit[len(domsplit) - 1]
                if domname in hashmap:
                    hashmap[domname] += int(domsplit[0])
                else:
                    hashmap[domname] = int(domsplit[0])
        output = []
        for key, value in hashmap.items():  # for each item, we format it as asked and add to the output
            output.append(str(value) + ' ' + key)
        return output
