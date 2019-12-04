Run the below command to save the decrypted message in flag.txt file:

openssl rsautl -decrypt -in flag.enc -out flag.txt -inkey private.pem

> cat flag.txt
