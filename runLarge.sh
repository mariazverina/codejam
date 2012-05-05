source probid.sh
echo Solving problem $PROBID try #$1
echo Started  `date` >> large.log
cat $PROBID*large*$1.in | python src/main.py script multi> $PROBID.large.out
echo Finished `date` >> large.log
cat $PROBID.large.out
sh mkzip.sh
