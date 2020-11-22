import subprocess


if __name__ == '__main__':
    subprocess.call('python3 community_gan.py dataset 0 n_emb 24 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset 107 n_emb 9 motif_size 3', shell=True, cwd='../src/CommunityGAN/')

    subprocess.call('python3 community_gan.py dataset 1912 n_emb 46 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset 3437 n_emb 32 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset 348 n_emb 14 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset 414 n_emb 7 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset 698 n_emb 13 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    
    subprocess.call('python3 community_gan.py dataset youtube n_emb 5 motif_size 3', shell=True, cwd='../src/CommunityGAN/')

    subprocess.call('python3 community_gan.py dataset amazon n_emb 5 motif_size 3', shell=True, cwd='../src/CommunityGAN/')

    subprocess.call('python3 community_gan.py dataset CiteSeer n_emb 6 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset Cora n_emb 7 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset Cora_ML_full n_emb 7 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset Cora_full n_emb 70 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset CiteSeer_full n_emb 6 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
    subprocess.call('python3 community_gan.py dataset dblp n_emb 5 motif_size 3', shell=True, cwd='../src/CommunityGAN/')
