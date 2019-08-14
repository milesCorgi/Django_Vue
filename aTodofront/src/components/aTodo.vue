<template>
  <div class="home">
    <div style="margin-top: 10px;margin-bottom: 10px">
      <el-row>
        <el-input v-model="input" placeholder="新Todo" style="display:inline-table; width: 30%"></el-input>
        <el-button type="primary" @click="addTodo">新增</el-button>
      </el-row>
    </div>

    <div>
      <el-row >
        <el-table :data="todoList" style="width: 100%" border>
          <el-table-column prop="book_name" label="Todo" min-width="100">
            <template scope="scope"> {{ scope.row.fields.Todo_body }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
                    <el-table-column prop="id" label="更新时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.update_time }} </template>
          </el-table-column>
          <el-table-column prop="id" label="状态" min-width="100">
            <template scope="scope"> {{ scope.row.fields.status }} </template>
          </el-table-column>
          <el-table-column label="操作" min-width="100">
            <template scope="scope">
              <i class="el-icon-edit" @click="openEditDialog(scope.row.pk)" style="cursor:pointer;margin-right: 20px">编辑</i>
              <i class="el-icon-delete" @click="delete_todo(scope.row.pk)" style="cursor:pointer" scope="scope">删除</i>
            </template>

          </el-table-column>
        </el-table>
      </el-row>
    </div>

    <el-dialog
      :visible.sync="openEditDialogFlag"
      @close="openEditDialogFlag = false">
      <el-input v-model ="toBeEditBody" type="input" style="display:inline-table; width: 50%"></el-input>
      <el-button type="primary" @click="editTodo">修改</el-button>
    </el-dialog>
  </div>
</template>

<script>
import Qs from 'qs'
export default {
  name: 'home',
  data () {
    return {
      input: '',
      todoList: [],
      openEditDialogFlag: false,
      toBeEditId: 0,
      toBeEditBody: ''
    }
  },
  mounted: function () {
    this.showtodos()
  },
  methods: {
    addTodo () {
      let posData = Qs.stringify({'Todo_body': this.input})
      this.$http.post('http://127.0.0.1:8000/api/add_todos', posData)
        .then((response) => {
          console.log(response)
          let res = response.data
          if (res.error_num === 0) {
            this.showtodos()
            this.input = ''
          } else {
            alert('新增Todo失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showtodos () {
      this.$http.get('http://127.0.0.1:8000/api/show_todos')
        .then((response) => {
          let res = response.data
          if (res.error_num === 0) {
            this.todoList = res['list']
            console.log(this.todoList)
          } else {
            this.$message.error('查询Todo失败')
            console.log(res['msg'])
          }
        })
    },
    delete_todo (id) {
      let postdata = Qs.stringify({'Todo_id': id})
      this.$http.post('http://127.0.0.1:8000/api/delete_todos', postdata)
        .then((response) => {
          console.log(response)
          let res = response.data
          if (res.error_num === 0) {
            this.showtodos()
          } else {
            alert('新增Todo失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    editTodo () {
      let posData = Qs.stringify({'Todo_body': this.toBeEditBody})
      this.$http.post('http://127.0.0.1:8000/api/edit_todos/' + this.toBeEditId, posData)
        .then((response) => {
          console.log(response)
          let res = response.data
          if (res.error_num === 0) {
            this.openEditDialogFlag = false
            this.showtodos()
          } else {
            alert('新增Todo失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    openEditDialog (id) {
      this.openEditDialogFlag = true
      this.toBeEditId = id
      this.$http.get('http://127.0.0.1:8000/api/edit_todos/' + this.toBeEditId)
        .then((response) => {
          let res = response.data
          if (res.error_num === 0) {
            console.log(res['list'][0].fields.Todo_body)
            this.toBeEditBody = res['list'][0].fields.Todo_body
          } else {
            this.$message.error('查询Todo失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
