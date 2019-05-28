template_head = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html" charset="GB2312 ">
<title>DT_hyhive</title>
<style> 
.css1{ width:280px;  solid #000; text-align:center; white-space: nowrap;text-overflow: ellipsis;overflow: hidden;  } 
.css2{ width:320px;  solid #000; white-space: nowrap;text-overflow: ellipsis;overflow: hidden;  } 
.css3{ solid #000; float:left;white-space: nowrap;text-overflow: ellipsis;overflow: hidden;  } 
</style> 
</head>
<body>
<p></p>
<p></p>
<table width="100%" border="1" style="table-layout:fixed">
<tr>
<td class="css1">time</td>
<td class="css1">path</td>
<td>stdout</td>
</tr>
"""

template_end = """
</table>
</body>
</html>
"""

template_info = """
<tr>
<td class="css1">time</td>
<td class="css2">path</td>
<td style="abbr:text">content</td>
</tr>
"""

template_warning = """
<tr>
<td class="css1">time</td>
<td class="css2">path</td>
<td style="abbr:text;bgcolor:0,0,0"><font color="red">content</font></td>
</tr>
"""
