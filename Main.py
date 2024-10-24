import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class BasketballStats:
    def __init__(self):
        self.stats_df = pd.DataFrame(columns=[
            'date', 'opponent', 'is_home', 'points', 
            'field_goals_made', 'field_goals_attempted',
            'three_pointers_made', 'three_pointers_attempted',
            'free_throws_made', 'free_throws_attempted',
            'rebounds', 'assists', 'steals'
        ])
    
    def add_game(self, date, opponent, is_home, points, fg_made, fg_attempted,
                 three_made, three_attempted, ft_made, ft_attempted,
                 rebounds, assists, steals):
        """Add a new game to the dataset"""
        new_game = pd.DataFrame([{
            'date': date,
            'opponent': opponent,
            'is_home': is_home,
            'points': points,
            'field_goals_made': fg_made,
            'field_goals_attempted': fg_attempted,
            'three_pointers_made': three_made,
            'three_pointers_attempted': three_attempted,
            'free_throws_made': ft_made,
            'free_throws_attempted': ft_attempted,
            'rebounds': rebounds,
            'assists': assists,
            'steals': steals
        }])
        self.stats_df = pd.concat([self.stats_df, new_game], ignore_index=True)
    
    def calculate_shooting_percentages(self):
        """Calculate shooting percentages for all shots"""
        self.stats_df['fg_percentage'] = (self.stats_df['field_goals_made'] / 
                                        self.stats_df['field_goals_attempted'] * 100).round(1)
        self.stats_df['three_percentage'] = (self.stats_df['three_pointers_made'] / 
                                           self.stats_df['three_pointers_attempted'] * 100).round(1)
        self.stats_df['ft_percentage'] = (self.stats_df['free_throws_made'] / 
                                        self.stats_df['free_throws_attempted'] * 100).round(1)
    
    def get_averages(self):
        """Calculate average stats per game"""
        return {
            'PPG': self.stats_df['points'].mean(),
            'FG%': self.stats_df['fg_percentage'].mean(),
            '3P%': self.stats_df['three_percentage'].mean(),
            'FT%': self.stats_df['ft_percentage'].mean(),
            'RPG': self.stats_df['rebounds'].mean(),
            'APG': self.stats_df['assists'].mean(),
            'SPG': self.stats_df['steals'].mean()
        }
    
    def plot_scoring_trend(self):
        """Plot scoring trend over time"""
        plt.figure(figsize=(12, 6))
        plt.plot(self.stats_df['date'], self.stats_df['points'], marker='o')
        plt.title('Scoring Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Points')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt

    def plot_shooting_percentages(self):
        """Plot shooting percentages comparison"""
        plt.figure(figsize=(10, 6))
        averages = self.get_averages()
        percentages = ['FG%', '3P%', 'FT%']
        values = [averages['FG%'], averages['3P%'], averages['FT%']]
        
        plt.bar(percentages, values)
        plt.title('Average Shooting Percentages')
        plt.ylabel('Percentage')
        plt.ylim(0, 100)
        
        for i, v in enumerate(values):
            plt.text(i, v + 1, f'{v:.1f}%', ha='center')
            
        plt.tight_layout()
        return plt

if __name__ == "__main__":
    stats = BasketballStats()
    
    stats.add_game(
        date='2024-10-15',
        opponent='Romao Rodrigues Branco',
        is_home=True,
        points=19,
        fg_made=6,
        fg_attempted=13,
        three_made=2,
        three_attempted=4,
        ft_made=1,
        ft_attempted=2,
        rebounds=11,
        assists=1,
        steals=2
    )
    
    stats.calculate_shooting_percentages()
    
    print("Season Averages:")
    for stat, value in stats.get_averages().items():
        print(f"{stat}: {value:.1f}")