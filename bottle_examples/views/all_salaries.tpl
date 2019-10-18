<table border="1">
    %for col_name in col_names:
        <td><b>{{col_name}}</b></td>
    %end

    %for row in rows:
        <tr>
        %for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    %end
</table>
