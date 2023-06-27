class CategoryTree:

    def __init__(self):
        self.tree_categories = {}

    def add_category(self, category, parent):
        ''' Adds a category '''
        if category in self.tree_categories:
          raise KeyError("category {category} already exists ".format(category=category))
        
        if parent is None: 
          if category in self.tree_categories.values():
            raise KeyError("category {category} already exists ".format(category=category))
          self.tree_categories[category] = None 
        else:
          if parent not in self.tree_categories:
            raise KeyError("parent category {parent} does not  exists ".format(parent=parent))
          self.tree_categories[category] = parent
          
    def get_children(self, parent):
        ''' Returns all the children of a parent in the category tree'''
        children = [] 
        for (key , value) in self.tree_categories.items():
           if value == parent :
               children.append(key)
        return children

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))