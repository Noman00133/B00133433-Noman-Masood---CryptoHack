# I used G'MIC tool to xor both images.
# Source: https://stackoverflow.com/questions/8504882/searching-for-a-way-to-do-bitwise-xor-on-images
# gmic flag.png lemur.png -blend xor -o cryptoflag.png

# I added the screenshots in the comment section.

# From terminal:

#┌──(b00133433㉿kali)-[~/College/Secure-Communications/CryptoHack/General]
#└─$ ls
#flag.png  lemur.png

#┌──(b00133433㉿kali)-[~/College/Secure-Communications/CryptoHack/General]
#└─$ gmic flag.png lemur.png -blend xor -o cryptoflag.png
#[gmic]-0./ Start G'MIC interpreter.
#[gmic]-0./ Input file 'flag.png' at position 0 (1 image 582x327x1x3).
#[gmic]-1./ Input file 'lemur.png' at position 1 (1 image 582x327x1x3).
#[gmic]-2./ Blend all images [0,1] together, using 'xor' mode and opacity 1.
#[gmic]-1./ Output image [0] as png file 'cryptoflag.png' (1 image 582x327x1x3).
#[gmic]-1./ End G'MIC interpreter.

#┌──(b00133433㉿kali)-[~/College/Secure-Communications/CryptoHack/General]
#└─$ 
