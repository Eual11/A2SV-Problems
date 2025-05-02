# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from typing import List
from collections import defaultdict

class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}

        def find(self, x):
            if x != self.parent.setdefault(x, x):
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            self.parent[self.find(x)] = self.find(y)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = self.UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        result = []
        for root_email, emails in groups.items():
            result.append([email_to_name[root_email]] + sorted(emails))
        return result
