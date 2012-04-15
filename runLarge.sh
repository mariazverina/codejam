source probid.sh
echo Solving problem $PROBID try #$1
date >> large.log
cat $PROBID*large*$1.in | python src/main.py script > $PROBID.large.out
date >> large.log
cat $PROBID.large.out
sh mkzip.sh
