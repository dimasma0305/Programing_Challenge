#$1="(123) 456-7890"
# check if the string is in the form of a phone number
# make "(" in the string to "\("

if echo $1 | grep -E "^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$" > /dev/null
then
    echo "True"
else
    echo "False"
fi
#or
regex='^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$'
[[ $1 =~ $regex ]] && echo True || echo False