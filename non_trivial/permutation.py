class Permutation:

    @staticmethod
    def permute(current, fixed_prefix=[], results = []):

        #TODO: permutation of string logic
        if not current:
            return results.append(fixed_prefix)

        if isinstance(current, str):
            current = [x for x in current]
        for i in range(len(current)):
            next_array = current[:i] + current[i+1:]
            Permutation.permute(next_array, fixed_prefix + [current[i]], results)

        return results



if __name__ == '__main__':
    print(Permutation.permute('ab))
