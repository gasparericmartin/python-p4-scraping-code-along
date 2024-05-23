class Course:
    def __init__(self, title='', schedule='', description=''):
        self.title = title
        self.schedule = schedule
        self.description = description
    
    def __repr__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------\n'
        return output
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def schedule(self):
        return self._schedule
    
    @schedule.setter
    def schedule(self, schedule):
        self._schedule = schedule
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description (self, description):
        self._description = description

