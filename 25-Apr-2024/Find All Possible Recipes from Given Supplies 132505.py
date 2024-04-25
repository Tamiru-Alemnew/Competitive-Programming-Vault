# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:   
        graph = defaultdict(list)
        incomming = defaultdict(int)

        for i in range(len(recipes)):
            current = recipes[i]

            for ingredient in ingredients[i]:
                graph[ingredient].append(current)
                incomming[current] += 1

        queue = deque()
        for recipe in recipes:
            if incomming[recipe] == 0 :
                queue.append(recipe)

        for supply in supplies :
            queue.append(supply)


        created_recipes = []

        while queue:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node in recipes:
                    created_recipes.append(node)

                for nbr in graph[node]:
                    incomming[nbr] -= 1

                    if incomming[nbr] == 0:
                        queue.append(nbr)

                
        return created_recipes
        

    