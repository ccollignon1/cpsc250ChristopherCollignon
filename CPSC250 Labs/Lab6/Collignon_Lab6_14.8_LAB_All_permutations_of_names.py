def print_all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.
    if len(nameList)==0:
        print(', '.join(permList))
    else:
        for x in range(len(nameList)):
            new_perm=permList + [nameList[x]]
            new_name=nameList[:x] + nameList[x+1:]
            print_all_permutations(new_perm,new_name)

if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)