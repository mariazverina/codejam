source probid.sh
echo Solving problem $PROBID try #$1
cat $PROBID*small*$1.in | python src/main.py multi script > $PROBID.small.out
cat $PROBID.small.out
sh mkzip.sh
