class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True
            arr1 = Counter(strs[i])

            for j in range(i + 1, len(strs)):
                if not visited[j] and Counter(strs[j]) == arr1:
                    group.append(strs[j])
                    visited[j] = True

            output.append(group)

        return output

