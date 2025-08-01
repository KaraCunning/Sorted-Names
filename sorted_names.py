Class Solution:
    
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ''' combining the names with heights, with the height first as that is  what we will be 
        sorting by. sort the list by height in descending order: reverse=True. Return just the 
        sorted names without the heights'''

        # create an empty list to hole the height and names       
        people = []

        # loop through the indexes and create pairs of heights and names. Height being first as this what
        # what we want to sort by
        for i in range(len(names)):
            pair = (heights[i], names[i])
            people.append(pair)

        # sort the pairs by the height in descending order
        people.sort(reverse=True)

        # create an empty list to store only the names of the sorted list
        sorted_names = []
        
        # get the name from the height
        for pair in people:
            sorted_names.append(pair[1])

        # return just the name from the sorted list
        return sorted_names

#End of Code