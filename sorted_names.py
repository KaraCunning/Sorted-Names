class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ''' combining the names with heights, with the height first as that is  what we will be sorting by. sort the list by height in descending order: reverse=True. Return just the sorted names without the heights'''
        people = list(zip(heights, names))
        
        people.sort(reverse=True)

        sorted_names=[name for heights, name in people]

        return sorted_names
       