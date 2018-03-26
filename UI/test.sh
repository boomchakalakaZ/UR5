# get list of tasks | get the tasks with python | remove extra spaces | split by space, get the second element
OUTPUT=`tasklist | grep python | sed "s/  */ /g" | cut -d" " -f2`

# convert string to array
arr=(${OUTPUT})

for i in "${arr[@]}"
do
    str="taskkill //PID $i //F"
    eval $str
done