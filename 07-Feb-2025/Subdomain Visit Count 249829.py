# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sub_domain_count = Counter()
        res =[]

        for cpd in cpdomains:
            visit, domains = cpd.split()
            visit = int(visit)

            sub_domain_count[domains] +=visit
            if(domains.count(".")!=2):
                idx = domains.rindex(".")
                sub_domain_count[domains[idx+1:]]+= visit
            else:

                idx = domains.index(".")
                sub_domain_count[domains[idx+1:]]+= visit

                idx = domains.rindex(".")
                sub_domain_count[domains[idx+1:]]+= visit
        for d, c in sub_domain_count.items():
            res.append(f"{c} {d}")
        return res
