#! /bin/bash 

bash join.sh train 7 queryid_tokensid.txt 1 >train1
bash join.sh train1 8 purchasedkeywordid_tokensid.txt 1 >train2
bash join.sh train2 9 titleid_tokensid.txt 1 >train3
bash join.sh train3 10 descriptionid_tokensid.txt 1 >train4
bash join.sh train4 11 userid_profile.txt 1 >train5
rm train1 train2 train3 train4
mv train5 train_combined
cat test | awk '{print NR "\t" $0}' > test_add
bash join.sh test_add 7 queryid_tokensid.txt 1 >test1
bash join.sh test1 8 purchasedkeywordid_tokensid.txt 1 >test2
bash join.sh test2 9 titleid_tokensid.txt 1 >test3
bash join.sh test3 10 descriptionid_tokensid.txt 1 >test4
bash join.sh test4 11 userid_profile.txt 1 >test5
rm test_add test1 test2 test3 test4
sort -n -t $'\t' -k 1,1 test5 >test_combined
rm test5
cat train_combined > t
cat test_combined >> t
python feature_map.py t t_map
head -n 1000000 t_map >train_data
tail -n 1000000 t_map >test_feature
rm t t_map
head -n 700000 train_data >train_feature
tail -n 300000 train_data >validata_feature
python train_ftrl.py
python auc.py pctr
