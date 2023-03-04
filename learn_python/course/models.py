import django.db.models
import course.validators


class Task(django.db.models.Model):
    title = django.db.models.CharField(
        verbose_name='Название', 
        max_length=150,
        unique=True,
    )
    time_limit = django.db.models.IntegerField(
        verbose_name='Ограничение времени (секунд)',
        default=1,
        validators=[course.validators.validate_more_zero],
    )
    memory_limit = django.db.models.IntegerField(
        verbose_name='Ограничение памяти (Mb)',
        default=64,
        validators=[course.validators.validate_more_zero],
    )
    text = django.db.models.TextField(
        verbose_name='Текст задания',
    )
    input_type = django.db.models.CharField(
        verbose_name='Ввод',
        max_length=100,
        default='стандартный ввод или input.txt',
    )
    output_type = django.db.models.CharField(
        verbose_name='Вывод',
        max_length=100,
        default='стандартный вывод или output.txt',
    )
    input_format = django.db.models.TextField(
        verbose_name='Формат ввода',
        blank=True,
        null=True,
    )
    output_format = django.db.models.TextField(
        verbose_name='Формат вывода',
        blank=True,
        null=True,
    )
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    
    def __str__(self) -> str:
        return self.title
    
    def get_time_limit(self) -> str:
        if 11 <= self.time_limit <= 19 or 5 <= self.time_limit % 10 <= 9 or self.time_limit % 10 == 0:
            return f'{self.time_limit} секунд'
        elif self.time_limit % 10 == 1:
            return f'{self.time_limit} секунда'
        elif 2 <= self.time_limit % 10 <= 4:
            return f'{self.time_limit} секунды'

    get_time_limit.allow_tags = True
    get_time_limit.short_description = 'Ограничение времени'

    def get_memory_limit(self) -> str:
        return f'{self.memory_limit}Mb'
    
    get_memory_limit.allow_tags = True
    get_memory_limit.short_description = 'Ограничение памяти'


class Example(django.db.models.Model):
    input_data = django.db.models.TextField(
        verbose_name='Ввод',
        blank=True,
        null=True,
    )
    output_data = django.db.models.TextField(
        verbose_name='Вывод',
        blank=True,
        null=True,
    )
    task = django.db.models.ForeignKey(
        verbose_name='Задание',
        to=Task,
        on_delete=django.db.models.CASCADE,
    )
    
    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'
    
    def __str__(self) -> str:
        return self.id
