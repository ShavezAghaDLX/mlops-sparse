from joblib import Memory

pipeline_config = {
  'joblib': {
    'clear_cache': True,
    'verbose': 0 # 0 for now messages, 1 for some messages, 2 for all messages  
    }
}

# Set cache directory
CACHE_DIR = './cachedir'
memory = Memory(CACHE_DIR, verbose=pipeline_config['joblib']['verbose'])

# Clear cache if needed
if pipeline_config['joblib']['clear_cache']:
    memory.clear(warn=True)