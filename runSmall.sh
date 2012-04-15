source probid.sh
echo Solving problem $PROBID try #$1
cat $PROBID*small*$1.in | python src/main.py > $PROBID.small.out
cat $PROBID.small.out
sh mkzip.sh
