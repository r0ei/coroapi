from coroapi import Corona

instance = Corona()
global_stats = instance.get_global_stats(text=False)

print(global_stats)
