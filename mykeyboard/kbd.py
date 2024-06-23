
class Key:

    def __init__(self, label, lower, upper):
        self.label = label
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"Key({self.label}, {self.lower}, {self.upper})"
    
class Keyboard:

    def __init__(self, tree):
        self.rows = []
        for row_elt in tree.getroot().findall("./row"):
            keys = []
            for key_elt in row_elt.findall("./key"):
                if len(key_elt.findall("./deleted")) != 0:
                    keys.append(None)
                else:
                    label_elt = key_elt.find("./label")
                    lower_elt = key_elt.find("./lower-letter")
                    upper_elt = key_elt.find("./upper-letter")
                    label = label_elt.text
                    lower = lower_elt.text if lower_elt != None else label.lower()
                    upper = upper_elt.text if upper_elt != None else label.upper()
                    keys.append(Key(label, lower, upper))
            self.rows.append(keys)

    @property
    def row_count(self):
        return len(self.rows)

    @property
    def column_count(self):
        return max(map(len, self.rows))
