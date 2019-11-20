x=`aws ec2 describe-regions | grep RegionName | cut -d '"' -f4`

for i in $x 
do

aws ec2 describe-images --owner 306761918474 --region $i


done
