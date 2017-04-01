#!/bin/bash
FORM_LOCATION="https://docs.google.com/forms/d/10yunl8d4HkAx6WfHEdarhKhK-9vc4VKY8f3qY64YC6Q/formResponse"
CODE_AREA="entry.1644658506"
ERROR_AREA="entry.727705083"
RSUB_EMAIL_AREA="entry.1527918066"
FILE_NAME_AREA="entry.780955098"
COMPILE_CALL_AREA="entry.2095423800"
errors=$(g++ -Wunused -Wfloat-equal -Wreturn-type $* 2>&1)
flags=""

#if [ "${errors}" != "" ] 
#then
    if [ "${UCRCS_COURSE}" == "CS010" -o "${UCRCS_COURSE}" == "CS010v" ]
    then
        if [ "$#" -gt 1 ]; then
            mkdir cmp_tmp &>/dev/null
            for var in "$@"
            do
                short=${var:0:1}
                if [ "$short" == "-" ]
                then
                    flags="${flags} $var"
                    continue
                fi
                
                myerrs=$(g++ -Wunused -Wfloat-equal -Wreturn-type $flags -c $var -o cmp_tmp/$var.o 2>&1)
                cpCall="g++ -Wunused -Wfloat-equal -Wreturn-type ${flags} -c ${var}"
                cp $var _no_name_tmp.cpp &>/dev/null
                sed -i "1,/END ASS/d" _no_name_tmp.cpp &>/dev/null
                value=$(cat _no_name_tmp.cpp 2>/dev/null)        
                rm _no_name_tmp.cpp &>/dev/null
                if [ "$value" == "" ]
                then
                    value=$(cat $var 2>/dev/null)
                fi
                code_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$value")"
                err_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$myerrs")"
                rsub_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$UCRCS_UCRSUB_EMAIL")"
                filenameCPP="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$var")"
                compilerCall="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$cpCall")"        
                curl "${FORM_LOCATION}?${CODE_AREA}=${code_val}&${ERROR_AREA}=${err_val}&${RSUB_EMAIL_AREA}=${rsub_val}&${FILE_NAME_AREA}=${filenameCPP}&${COMPILE_CALL_AREA}=${compilerCall}" &>/dev/null
            done
            rm -rf cmp_tmp &>/dev/null
        elif [ "$#" -gt 0 ]; then
            cp $var _no_name_tmp.cpp &>/dev/null
            sed -i "1,/END ASS/d" _no_name_tmp.cpp &>/dev/null
            value=$(cat _no_name_tmp.cpp 2>/dev/null)        
            rm _no_name_tmp.cpp &>/dev/null
            if [ "$value" == "" ]
            then
                value=$(cat $1 2>/dev/null)
            fi
            cpCall="g++ -Wunused -Wfloat-equal -Wreturn-type $*"
            code_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$value")"
            err_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$errors")"
            rsub_val="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$UCRCS_UCRSUB_EMAIL")"    
            filenameCPP="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$1")"
            compilerCall="$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$cpCall")"                    
            curl "${FORM_LOCATION}?${CODE_AREA}=${code_val}&${ERROR_AREA}=${err_val}&${RSUB_EMAIL_AREA}=${rsub_val}&${FILE_NAME_AREA}=${filenameCPP}&${COMPILE_CALL_AREA}=${compilerCall}" &>/dev/null
        fi
    fi
    echo "$errors"
#fi

