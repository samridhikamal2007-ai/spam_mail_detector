import os
import argparse
import pandas as pd
import requests

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def download_sms_spam(dest_path):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
    r = requests.get(url)
    r.raise_for_status()
    import zipfile, io
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(os.path.dirname(dest_path))

def load_sms_spam(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'SMSSpamCollection')
    df = pd.read_csv(path, sep='\t', header=None, names=['label','message'])
    df['label'] = df['label'].map({'ham':0, 'spam':1})
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--download', action='store_true')
    args = parser.parse_args()
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    os.makedirs(data_dir, exist_ok=True)
    dest = os.path.join(data_dir, 'SMSSpamCollection')
    if args.download:
        print('Downloading dataset...')
        download_sms_spam(dest)
        print('Downloaded and extracted to', data_dir)
    df = load_sms_spam(dest)
    csv_path = os.path.join(data_dir, 'smsspam.csv')
    df.to_csv(csv_path, index=False)
    print('Saved CSV to', csv_path)

if __name__ == '__main__':
    main()
