# for p in Mutliclass_Barabasi_Xtrain AMD_Mutliclass_Barabasi_Xtrain PRAD_Barabasi_Xtrain LUSC_Barabasi_Xtrain LUAD_Barabasi_Xtrain KICH_Barabasi_Xtrain COAD_Barabasi_Xtrain BRCA2_Barabasi_Xtrain
# 	do
# 		./test ${p}.csv > ${p}
# 	done
for p in DTAin
	do
		./test ${p}.csv > ${p}		
		for i in 5 10 15 20 30 40
			do
			#	echo "./feature_single -i ${p} -k ${i} -epsilon 0.01 -delta 0 -m IC -alg DTA > ${p}_${i}_single"
				./feature -i ${p} -k ${i} -epsilon 0.002 -delta 0 -m IC -alg DTA > ${p}_${i}
				tail -5 ${p}_${i} > log
				head -1 log > ${p}_${i}
			done
	done

