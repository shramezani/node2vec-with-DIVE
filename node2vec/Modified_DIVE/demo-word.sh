make
if [ ! -e text8 ]; then
  wget http://mattmahoney.net/dc/text8.zip -O text8.gz
  gzip -d text8.gz -f
fi
time ./word2vec -train raw_data -output vectors___init2_context_D_50_S_3_K_03.bin -save-vocab vocab -alpha 0.50 -window 10 -cbow 0 -sample 1e-3 -threads 20 -binary 1 -iter 15
./distance vectors___init2_context_D_50_S_3_K_03.bin

# init1 --> same initialization for input and output layers
# init2 --> differnt initialization for input and output layers
