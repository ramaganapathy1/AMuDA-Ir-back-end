echo "training data file Generation"

#python ml_audio/write_all.py CG1.tab,comparch1.tab,dbms1.tab,ds1.tab,iit-k-psp-Ipsp-lec1.tab,it1.tab,ml1.tab,ppl1.tab TrainingDataSet_introLecturesCS.tab output keys TrainingDataSet Porter-Stemmer

#python ml_audio/write_all.py cg5.tab,dbms-DBMS-lecture-2.tab,dbms-lec18.tab,ds2.tab,ds4.tab,ds5.tab,ds6.tab,ds7.tab,iit-d-ca-CA-LEC3.tab,iit-d-ca-CA-LEC9.tab,iit-d-ca-CA-LEC-5.tab,ml4.tab,ml5.tab,ml6.tab,ml8.tab,ml10.tab TrainingDataSet_illusLecturesCS.tab output keys TrainingDataSet Porter-Stemmer

#python ml_audio/write_all.py ds3.tab,ds11.tab,ds13.tab,iit-d-ca-CA-LEC-2.tab,iit-d-ca-CA-LEC-6.tab,iit-d-ca-CA-LEC-7.tab,ppl2.tab,ppl3.tab,ppl4.tab,ppl5.tab TrainingDataSet_descriptiveCS.tab output keys TrainingDataSet Porter-Stemmer

#python ml_audio/write_all.py CG1.tab,comparch1.tab,dbms1.tab,ds1.tab,iit-k-psp-Ipsp-lec1.tab,it1.tab,ml1.tab,ppl1.tab,iit-d-ca-CA-LEC3.tab,iit-d-ca-CA-LEC9.tab,iit-d-ca-CA-LEC-5.tab,ml5.tab,ml6.tab,ml8.tab,ml10.tab,ppl2.tab,ppl3.tab,ppl4.tab,ppl5.tab TrainingDataSet_illustrative_desc_intro.tab output keys TrainingDataSet Porter-Stemmer

python ml_audio/write_all.py bio1.tab,biochem2.tab,cg2.tab,cg3.tab,CG1.tab,comparch1.tab,dbms1.tab,ds1.tab,ds2.tab,ds5.tab,ds6.tab,ml1.tab,ml3.tab,ppl1.tab,ppl3.tab Train_the_test_data.tab output keys TrainTheTest Porter-Stemmer


echo "done"
